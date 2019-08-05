import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    session["user_id"]

    """Show portfolio of stocks"""
    if request.method=="POST":
        if not request.form.get("addcash"):
            return apology("Please enter cash to add", 400)
        else:
            addcash=request.form.get("addcash")
            cash=db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
            db.execute("UPDATE users SET cash = cash + :addcash  WHERE id = :id", \
            id=session["user_id"], \
            addcash=addcash)
            flash('$' + addcash + ' added!')
            return redirect("/")
    else:
     shares=db.execute("SELECT share FROM portfolio WHERE id=:id", id=session["user_id"])
     portfolio=[]
     totalvalue=0
     cash=db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
     ucash=cash[0]["cash"]
     for x in shares:
        share=x["share"]
        numshares=db.execute("SELECT numshares FROM portfolio WHERE id=:id AND share=:share",
        id=session["user_id"],
        share=share)
        numshare=int(numshares[0]["numshares"])
        stock=lookup(x["share"])
        price=stock["price"]
        value=price * numshare
        totalvalue+=value
        portfolio.append({"share":share, "numshare":numshare, "price":price, "value":value});

     return render_template("index.html", portfolio=portfolio, totalvalue=usd(totalvalue), ucash=usd(ucash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    session["user_id"]
    if request.method=="POST":
        if not request.form.get("symbol"):
            return apology("Please enter a symbol to lookup")
        elif not request.form.get("shares"):
            return apology("Please enter a number of shares to buy")
        #code borrowed from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
        elif int(request.form.get("shares")) < 0:
            return apology("Please enter an integer for # of shares")
        elif lookup(request.form.get("symbol"))==None:
            return apology("Please enter a valid symbol")
        else:
            share=request.form.get("symbol")
            get_cash=db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
            cash=get_cash[0]["cash"]
            stock=lookup(share)
            price=stock["price"]
            shares=int(request.form.get("shares"))
            cost=shares * price

        if cost > float(cash):
                return apology("User does not have enough cash", 400)

        db.execute("UPDATE users SET cash = cash - :cost WHERE id = :id", \
            id=session["user_id"], \
            cost=cost)

        current_shares=db.execute("SELECT share FROM portfolio WHERE id=:id AND share=:share", \
        id=session["user_id"], \
        share=share)

        if not current_shares:
            db.execute("INSERT INTO portfolio (id, share, numshares, price) VALUES (:id, :share, :shares, :price)", \
            id=session["user_id"], \
            share=share,\
            shares=shares, \
            price=price)
        else:
            db.execute("UPDATE portfolio SET numshares=numshares + :shares WHERE id=:id AND share=:share", id=session["user_id"], share=stock["symbol"], shares=shares)

        #Store buy in transactions history
        db.execute("INSERT INTO transactions (id, share, shares, price, transtype) VALUES (:id, :share, :shares, :price, :transtype)", \
        id=session["user_id"], \
        share=share,\
        shares=shares,\
        price=price,\
        transtype="buy")
        flash('Shares successfully purchased!')

        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username=request.args.get("username", "")
    users=db.execute("SELECT username FROM users WHERE username=:username", username=username)

    if users or len(username)==0:
        return jsonify(False)
    else:
        return jsonify(True)


@app.route("/history")
@login_required
def history():
    session["user_id"]

    """Show history of transactions"""

    history=db.execute("SELECT * FROM transactions WHERE id=:id", id=session["user_id"])
    if not history:
        return apology("No history for user", 400)
    else:
        return render_template("history.html", history=history)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    session["user_id"]
    if request.method=="POST":
        if not request.form.get("symbol"):
            return apology("Please enter a stock symbol", 400)
        else:
            quote=lookup(request.form.get("symbol"))
            return render_template("quoted.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method=="POST":
    #Ensure username was entered
      if not request.form.get("username"):
         return apology("Must enter a username", 400)

    #Ensure password was entered
      elif not request.form.get("password"):
         return apology("Must enter a password", 400)

    #Ensure password was confirmed
      elif not request.form.get("confirmation"):
         return apology("Please confirm your password", 400)
      elif request.form.get("password") != request.form.get("confirmation"):
         return apology("Password and confirmation must match!", 400)
      else:
        hash=generate_password_hash(request.form.get("password"))
        result=db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
        username=request.form.get("username"),
        hash=hash)
        return redirect("/")
        if not result:
            return apology("This username already exists, please enter a different one", 400)
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    session["user_id"]

    #Ensure form is filled out correctly
    if request.method=="POST":
        if not request.form.get("symbol"):
            return apology("Please enter a symbol", 400)
        elif not request.form.get("shares"):
            return apology("Please enter a number of shares", 400)
        elif int(request.form.get("shares")) < 0:
            return apology("Number of shares must be an integer", 400)
        else:
            #Get form values, and user information from DB to update
            share=request.form.get("symbol")
            sellshares=int(request.form.get("shares"))
            shares=db.execute("SELECT share FROM portfolio WHERE id=:id", \
            id=session["user_id"])
            numshares=db.execute("SELECT numshares FROM portfolio WHERE share=:share AND id=:id", \
            share=share,
            id=session["user_id"])
            numshares=numshares[0]["numshares"]


            #Check if user has enough stock to sell
            if numshares < sellshares:
             return apology("Not enough shares to sell", 400)
            curstock=lookup(share)
            currentprice=curstock["price"]
            profit=currentprice * sellshares

            #Check whether selling all or some shares
            if numshares > sellshares:
               db.execute("UPDATE portfolio SET numshares=numshares - :sellshares WHERE id=:id AND share=:share", \
               sellshares=sellshares,
               id=session["user_id"],
               share=share)
            else:
              db.execute("DELETE FROM portfolio WHERE id=:id AND share=:share", \
              id=session["user_id"],
              share=request.form.get("symbol"))

        db.execute("UPDATE users SET cash = cash + :profit WHERE id = :id", \
        id=session["user_id"], \
        profit=profit)

         #Store sell in transactions history
        db.execute("INSERT INTO transactions (id, share, shares, transtype, price) VALUES (:id, :share, :shares, :transtype, :currentprice)", \
        id=session["user_id"],
        share=share,
        shares=sellshares,
        currentprice=currentprice,
        transtype="sell")

        flash('Shares successfully sold!')
        #Take user back to home page
        return redirect("/")

    else:
        shares=db.execute("SELECT share FROM portfolio WHERE id=:id", \
         id=session["user_id"])
        return render_template("sell.html", shares=shares)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

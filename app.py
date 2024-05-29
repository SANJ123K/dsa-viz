from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("layout.html")


@app.route("/visualization")
def visualization_():
    return render_template("visualization.html")

################################### sorting #########################


@app.route("/sorting-algo")
def sorting():
    return render_template("sorting.html")


@app.route("/sorting-insertion")
def insertion():
    return render_template("sorting/insertionsort.html")


@app.route("/sorting-selection")
def selection():
    return render_template("sorting/selectionsort.html")


@app.route("/sorting-bubble")
def bubble():
    return render_template("sorting/bubblesort.html")


@app.route("/sorting-merge")
def merge():
    return render_template("sorting/mergesort.html")


@app.route("/sorting-quick")
def quick():
    return render_template("sorting/quicksort.html")

######################################## Stack ##############################


@app.route("/stack")
def stack():
    return render_template("stack/stack.html")


#####################################  Queue ##################################

@app.route("/queue")
def queue():
    return render_template("queue.html")


@app.route("/simple-queue")
def simple_queue():
    return render_template("queueds/simplequeue.html")


@app.route("/double-ended-queue")
def double_ended_queue():
    return render_template("queueds/duble_ended.html")


@app.route("/circular-queue")
def circular_queue():
    return render_template("queueds/circular_queue.html")


################################# Linked List #####################################33


@app.route("/linked-list")
def linked_list():
    return render_template("linkedlist/linked_list.html")


############################### Tree ##########################


@app.route("/tree")
def tree():
    return render_template("/treeds/tree.html")


########################## graph #############################

@app.route("/graph")
def graph():
    return render_template("graph.html")


if __name__ == "__main__":
    app.run(debug=True)

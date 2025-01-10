from flask import Flask, render_template, request, redirect, url_for, flash
import heapq
from collections import deque

app = Flask(__name__)
app.secret_key = "b2e5f8c2a4d942d8bb213f3d1c4f4d8b"

def convert_seat_id(row, col):
    alphabet = chr(64 + row) 
    return f"{alphabet}{col}"

# Graph to represent seats
class SeatGraph:
    def __init__(self, rows, cols):
        self.graph = {convert_seat_id(r, c): [] for r in range(1, rows+1) for c in range(1, cols+1)}
        self.create_edges(rows, cols)

    def create_edges(self, rows, cols):
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                current = convert_seat_id(r, c)
                if c < cols:
                    self.graph[current].append(convert_seat_id(r, c+1))
                if r < rows:
                    self.graph[current].append(convert_seat_id(r+1, c))

    def get_neighbors(self, seat):
        return self.graph[seat]

# Priority Queue for VIP booking
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, item):
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0

# Queue for regular bookings
booking_queue = deque()

vip_queue = PriorityQueue()

seat_graph = SeatGraph(10, 10)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book', methods=['GET', 'POST'])
def book_ticket():
    if request.method == 'GET':
        seat = request.args.get('seat')
        seats = list(seat_graph.graph.keys())
        return render_template('book.html', seat=seat, seats=seats)
    elif request.method == 'POST':
        name = request.form['name']
        seat = request.form['seat']
        priority = request.form['priority']
        flash(f"Ticket booked for {name} at seat {seat} with {priority} priority!")
        return redirect(url_for('seats'))

@app.route('/seats')
@app.route('/seats/<movie>')
def seats(movie=None):
    return render_template('seats.html', seats=seat_graph.graph.keys(), movie_name=movie)

if __name__ == '__main__':
    app.run(debug=True)

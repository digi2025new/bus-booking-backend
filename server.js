const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

let seats = [
    { id: 1, status: "available" },
    { id: 2, status: "available" },
    { id: 3, status: "booked" },
    { id: 4, status: "available" },
    { id: 5, status: "available" }
];

// Get seats
app.get("/seats", (req, res) => {
    res.json(seats);
});

// Book a seat
app.post("/book/:id", (req, res) => {
    const seatId = parseInt(req.params.id);
    const seat = seats.find(s => s.id === seatId);
    
    if (seat && seat.status === "available") {
        seat.status = "booked";
        res.json({ message: "Seat booked successfully!" });
    } else {
        res.status(400).json({ error: "Seat not available" });
    }
});

app.listen(5000, () => {
    console.log("Server running on http://localhost:5000");
});

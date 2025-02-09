import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Tracker.css"; // ✅ Import styling

const Tracker = () => {
  const navigate = useNavigate(); // ✅ Hook for navigation

  // ✅ State for dynamic routes
  const [routes, setRoutes] = useState([{ id: 1, start: "", end: "" }]);
  const [transportation, setTransportation] = useState(""); // ✅ Mode of transport
  const [usedCar, setUsedCar] = useState(null); // ✅ Car usage state
  const [make, setMake] = useState(""); // ✅ Car make
  const [model, setModel] = useState(""); // ✅ Car model
  const [carpool, setCarpool] = useState(""); // ✅ Carpooling status
  const [rating, setRating] = useState(0); // ✅ Fuel efficiency rating
  const [publicTransport, setPublicTransport] = useState(null); // ✅ Public transport usage
  const [walkedOrBiked, setWalkedOrBiked] = useState(null); // ✅ Walking/biking usage

  // ✅ Function to add new routes dynamically
  const addRoute = () => {
    setRoutes([...routes, { id: routes.length + 1, start: "", end: "" }]);
  };

  // ✅ Function to delete a route (ensuring at least one route remains)
  const deleteRoute = (id) => {
    if (routes.length === 1) return;
    setRoutes(routes.filter((route) => route.id !== id));
  };

  // ✅ Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("🔍 Submitting tracker data...");

    const token = localStorage.getItem("token"); // ✅ Retrieve user token

    // ✅ Prepare travel data correctly
    const travelData = routes.map((route) => ({
      start_location: route.start,
      end_location: route.end,
      mode_of_transport: transportation,
    }));

    // ✅ Construct payload matching working cURL
    const payload = {
      log_id: "123", // ✅ Always set to "123"
      travel: travelData,
      car_usage: usedCar === "yes" ? { make, model, carpool_status: carpool } : {},
      public_transport: publicTransport !== null ? { used_public_transport: publicTransport } : {},
      active_travel: walkedOrBiked !== null ? { walked_or_biked: walkedOrBiked } : {},
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/carbon/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`, // ✅ Include user token
        },
        body: JSON.stringify(payload), // ✅ Send JSON correctly
      });

      const responseData = await response.json();

      if (response.ok) {
        console.log("✅ Carbon footprint submitted successfully:", responseData);
        navigate("/login"); // ✅ Redirect to dashboard
      } else {
        console.error("❌ Submission failed:", responseData);
        alert(`Error: ${responseData.detail}`); // ✅ Show error to user
      }
    } catch (error) {
      console.error("❌ Network or Server Error:", error);
      alert("An error occurred. Please try again later.");
    }
  };

  return (
    <div className="tracker-container">
      <h1>Travel Tracker Form</h1>
      <form>
        {/* Travel Section */}
        <div className="section">
          <div className="section-title">Travel</div>
          <h1 className="section-subtitle">Where did you travel today?</h1>
          {routes.map((route) => (
            <div className="form-group route-group" key={route.id}>
              <div className="route-number">
                Route {route.id}
                {routes.length > 1 && (
                  <span
                    className="delete-route"
                    onClick={() => deleteRoute(route.id)}
                    title="Delete this route"
                  >
                    &times;
                  </span>
                )}
              </div>
              <label htmlFor={`start-location-${route.id}`}>Start Route</label>
              <input
                type="text"
                id={`start-location-${route.id}`}
                name={`start-location-${route.id}`}
                placeholder="Enter Start Route"
                required
              />
              <label htmlFor={`end-location-${route.id}`}>End Route</label>
              <input
                type="text"
                id={`end-location-${route.id}`}
                name={`end-location-${route.id}`}
                placeholder="Enter End Route"
                required
              />
            </div>
          ))}
          <div className="addroute-button" onClick={addRoute}>Add Route</div>

          <div className="form-group">
            <label htmlFor="transportation">
              What mode of transportation did you use?
            </label>
            <select id="transportation" name="transportation">
              <option value="">--Select--</option>
              <option value="car">Car</option>
              <option value="ev">Electric Vehicle</option>
              <option value="bike">Bike</option>
              <option value="public">Public Transport</option>
              <option value="walking">Walking</option>
            </select>
          </div>
        </div>

        {/* Car Usage Section */}
        <div className="section">
          <div className="section-title">Car Usage</div>
          <div className="form-group">
            <label>Did you use a car today?</label>
            <div className="radio-group">
              <label>
                <input
                  type="radio"
                  name="used-car"
                  value="yes"
                  onChange={() => setUsedCar("yes")}
                /> Yes
              </label>
              <label>
                <input
                  type="radio"
                  name="used-car"
                  value="no"
                  onChange={() => setUsedCar("no")}
                /> No
              </label>
            </div>
          </div>
          {usedCar === "yes" && (
            <>
              <div className="form-group make-model-group">
                <label htmlFor="make">What type of car?</label>
                <input
                  type="text"
                  id="make"
                  name="make"
                  placeholder="Make"
                  required
                />
                <input
                  type="text"
                  id="model"
                  name="model"
                  placeholder="Model"
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="carpool">Did you carpool or drive solo?</label>
                <select id="carpool" name="carpool">
                  <option value="">--Select--</option>
                  <option value="solo">Solo</option>
                  <option value="1-2">1-2 passengers</option>
                  <option value="3+">3+ passengers</option>
                </select>
              </div>
              <div className="form-group">
                <label>
                  On a scale of 1-5, how fuel-efficient were your chosen route options?
                </label>
                <div className="rating-container">
                  {[1, 2, 3, 4, 5].map((num) => (
                    <div
                      key={num}
                      className={`rating-box ${rating === num ? "selected" : ""}`}
                      onClick={() => setRating(num)}
                    >
                      {num}
                    </div>
                  ))}
                </div>
              </div>
            </>
          )}
        </div>

        {/* Public Transport & Shared Rides Section */}
        <div className="section">
          <div className="section-title">
            Public Transportation & Shared Rides
          </div>
          <div className="form-group">
            <label>
              Did you use public transportation or ride share today (train, bus, uber)?
            </label>
            <div className="radio-group">
              <label>
                <input type="radio" name="public-transport" value="yes" /> Yes
              </label>
              <label>
                <input type="radio" name="public-transport" value="no" /> No
              </label>
            </div>
          </div>
        </div>

        {/* Walk/Bike Section */}
        <div className="section">
          <div className="section-title">Walk/Bike</div>
          <div className="form-group">
            <label>Did you walk or bike today?</label>
            <div className="radio-group">
              <label>
                <input type="radio" name="walk-bike" value="yes" /> Yes
              </label>
              <label>
                <input type="radio" name="walk-bike" value="no" /> No
              </label>
            </div>
          </div>
        </div>

        {/* Eco-Friendly Travel Choices Section */}
        <div className="section">
          <div className="section-title">Eco-Friendly Travel Choices</div>
          <div className="form-group">
            <label htmlFor="sustainable-option">
              Would you consider a more sustainable travel option next time?
            </label>
            <select id="sustainable-option" name="sustainable-option">
              <option value="">--Select--</option>
              <option value="yes">Yes</option>
              <option value="no">No</option>
              <option value="unsure">Maybe</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="habit-improve">
              (OPTIONAL) What’s one small transportation habit you’d like to improve tomorrow?
            </label>
            <textarea
              id="habit-improve"
              name="habit-improve"
              rows="3"
              placeholder="Enter your idea..."
            ></textarea>
          </div>
          <div className="form-group">
            <label htmlFor="sustainable-action">
              (OPTIONAL) What was one sustainable action you actively tried today?
            </label>
            <textarea
              id="sustainable-action"
              name="sustainable-action"
              rows="3"
              placeholder="Enter your action..."
            ></textarea>
          </div>
          <div className="form-group">
            <label htmlFor="eco-choice">
              (OPTIONAL) What eco-friendly travel choice did you make today that you’re most proud of?
            </label>
            <textarea
              id="eco-choice"
              name="eco-choice"
              rows="3"
              placeholder="Enter your choice..."
            ></textarea>
          </div>
        </div>

        <button type="submit">Submit Tracker</button>
      </form>
    </div>
  );
};

export default Tracker;

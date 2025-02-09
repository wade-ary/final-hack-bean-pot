// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Navbar from "./Navbar.js";
import Home from "./homepage/Home.js";
import Info from "./Info";
import Tracker from "./Tracker";
import Analytics from "./Analytics.js";
import Signup from "./Signup.js";
import Login from "./Login.js";


function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <div className="content">
          <Routes>
            <Route path="/" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/home" element={<Home />} />
            <Route path="/info" element={<Info />} />
            <Route path="/tracker" element={<Tracker />} />
            <Route path="/analytics" element={<Analytics />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;



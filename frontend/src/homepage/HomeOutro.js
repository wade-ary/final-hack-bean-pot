// src/HomeOutro.js
import React from "react";
import "./HomeOutro.css";
import { Link } from "react-router-dom";

const HomeOutro = () => {
  return (
    <section className="outro-section">
      {/* Top: Centered Text */}
      <div className="outro-text">
        <h1>Header 1</h1> 
        <p>This is the first paragraph of text explaining something important.</p>
      </div>

      {/* Bottom: Row of Images */}
      <div className="outro-image">
        <img src="/picture.png" alt="Description of the image" />
      </div>

    <div className="button-container">
      <Link to="/tracker">
        <button className="navigate-button">Go to Tracker</button>
      </Link>
    </div>

    </section>
  );
};

export default HomeOutro;


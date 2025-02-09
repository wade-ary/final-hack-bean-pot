// src/HomeHero.js
import React from "react";
import "./HomeHero.css"; // import the CSS file for styling

const HomeHero = () => {
  return (
    <section className="hero-container">
      <div className="hero-text">
        <h1>Welcome to Carbon Tracker</h1>
        <p>
          Discover how small changes in your travel habits can create a big
          impact on our planet. Let's drive sustainable change together.
        </p>
      </div>
      <div className="hero-image">
        <img
          src="/picture.png" alt="Eco-friendly travel"
        />
      </div>
    </section>
  );
};

export default HomeHero;

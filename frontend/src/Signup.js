// src/SignUp.js
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Signup.css";


const SignUp = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");


  // ✅ Handle input changes
  const handleUsernameChange = (e) => setUsername(e.target.value);
  const handleEmailChange = (e) => setEmail(e.target.value);
  const handlePasswordChange = (e) => setPassword(e.target.value);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("🔍 Sending data:", { username, email, password });

    const response = await fetch("http://127.0.0.1:8000/user_auth/signup", {

      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
                                 
      body: JSON.stringify({ username, email, password }),
    });

    if (response.ok) {
      console.log("✅ Signup successful");
      navigate("/home");
    } else {
      console.error("❌ Signup failed");
    }
  };

  return (
    <div className="signup-container">
      <div className="signup-left">
        <h1>Sign Up</h1>
        <form onSubmit={handleSubmit}>
          <div className="name-fields">
            <input
              type="text"
              placeholder="Username"
              required
              value={username}
              onChange={handleUsernameChange} // ✅ Capture input
            />
          </div>
          <input
            type="email"
            placeholder="Email"
            required
            value={email}
            onChange={handleEmailChange} // ✅ Capture input
          />
          <input
            type="password"
            placeholder="Password"
            required
            value={password}
            onChange={handlePasswordChange} // ✅ Capture input
          />
          <button type="submit">Sign Up</button>
        </form>
        <div className="signup-footer">
          <hr className="divider" />
          <p>
            Already have an account? <Link to="/login">Log in here</Link>
          </p>
        </div>
      </div>
      <div className="signup-right">
        <img src="/picture.png" alt="Sign Up" />
      </div>
    </div>
  );
};

export default SignUp;

// hilllllldlflsldflsldflsldlf
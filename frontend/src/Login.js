// src/Login.js
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Login.css";


const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // ✅ Handle input changes
  const handleEmailChange = (e) => setEmail(e.target.value);
  const handlePasswordChange = (e) => setPassword(e.target.value);

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const email = e.target.email.value;   // Fetch email from input field
    const password = e.target.password.value; // Fetch password
  
    console.log("📤 Sending request:", { email, password }); // ✅ Debugging output
  
    try {
      const response = await fetch("http://127.0.0.1:8000/user_auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }), // ✅ Ensure proper JSON formatting
      });
  
      const data = await response.json();
      console.log("📥 Received response:", data);
  
      if (response.ok) {
        console.log("✅ Login successful");
        navigate("/home"); // Redirect on success
      } else {
        console.error("❌ Login failed:", data.detail);
      }
    } catch (error) {
      console.error("❌ Network error:", error);
    }
  };

  return (
    <div className="login-container">
      <div className="login-left">
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
  <input type="email" name="email" placeholder="Email" required />
  <input type="password" name="password" placeholder="Password" required />
  <button type="submit">Log in</button>
</form>
        <div className="login-footer">
          <hr className="divider" />
          <p>
            Don't have an account? <Link to="/">Sign Up Here</Link>
          </p>
        </div>
      </div>
      <div className="login-right">
        <img src="/picture.png" alt="Login" />
      </div>
    </div>
  );
};

export default Login;


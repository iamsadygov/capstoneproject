import React from "react";
import { Link } from "react-router-dom";
import "./layout.css";
import logo from "./laptop_2428922.png";

const Layout = ({ children }) => {
  return (
    <>
      <nav className="navbar">
        {/* Logo Section */}
        <div className="nav-logo-container">
          <img src={logo} alt="Logo" className="nav-logo" />
        </div>

        {/* Navigation Links */}
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/ranking">Ranking</Link>
        </div>
      </nav>

      <main className="layout-content">{children}</main>
    </>
  );
};

export default Layout;

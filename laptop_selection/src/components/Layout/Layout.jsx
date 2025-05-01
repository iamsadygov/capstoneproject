import React, { useState, useEffect, useRef } from "react";
import { Link, useLocation } from "react-router-dom";
import "./layout.css";
import logo from "./laptop_2428922.png";


const Layout = ({ children, onBrandSelect }) => {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [brands, setBrands] = useState([]);
  const [loading, setLoading] = useState(true);
  const dropdownRef = useRef(null);
  const location = useLocation();

  // 📌 Fetch Brands from JSON (Ensure JSON is in public folder)
  useEffect(() => {
    fetch("/laptops.json")
      .then((response) => response.json())
      .then((data) => {
        const uniqueBrands = ["All", ...new Set(data
          .map((laptop) => laptop.Brand?.trim())
          .filter(brand => brand && brand.length > 1) // Remove invalid brands
        )];
        setBrands(uniqueBrands.sort());
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching brands:", error);
        setLoading(false);
      });
  }, []);

  // 📌 Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setDropdownOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // 📌 Close dropdown when changing pages
  useEffect(() => {
    setDropdownOpen(false);
  }, [location.pathname]);

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

          {/* Dropdown for Brands */}
          <div className="dropdown" ref={dropdownRef}>
            <button className="dropdown-btn" onClick={() => setDropdownOpen(!dropdownOpen)}>
              Brands ▾
            </button>
            {dropdownOpen && (
              <div className="dropdown-menu">
                {loading ? (
                  <div className="dropdown-item">Loading...</div>
                ) : (
                  brands.map((brand) => (
                    <div
                      key={brand}
                      className="dropdown-item"
                      onClick={() => {
                        onBrandSelect(brand); // Updates selected brand
                        setDropdownOpen(false);
                      }}
                    >
                      {brand.charAt(0).toUpperCase() + brand.slice(1)} {/* Capitalize brands */}
                    </div>
                  ))
                )}
              </div>
            )}
          </div>

          <Link to="/ranking">Personalized Ranking</Link>
        </div>

       
      </nav>

      <main className="layout-content">{children}</main>
    </>
  );
};

export default Layout;

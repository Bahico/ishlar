import React from 'react';
import "../home/css/templatemo-xtra-blog.css";
import "../home/css/bootstrap.min.css"
import {Link} from "react-router-dom";

const Navbar = () => {
    const active = name => {
        if (name === "home") {
            document.querySelector(".nav_home").className = "tm-nav-item nav_home active";
            document.querySelector(".nav_about").className = "nav_about tm-nav-item";
            document.querySelector(".nav_contact").className = "nav_contact tm-nav-item";
            document.querySelector(".nav_login").className = "tm-nav-item nav_login";
        } else if (name === "about") {
            document.querySelector(".nav_home").className = "tm-nav-item nav_home ";
            document.querySelector(".nav_about").className = "tm-nav-item active nav_about";
            document.querySelector(".nav_contact").className = "tm-nav-item nav_contact";
            document.querySelector(".nav_login").className = "tm-nav-item nav_login";
        } else if (name === "contact") {
            document.querySelector(".nav_home").className = "nav_home tm-nav-item";
            document.querySelector(".nav_about").className = "tm-nav-item nav_about";
            document.querySelector(".nav_contact").className = "tm-nav-item active nav_contact";
            document.querySelector(".nav_login").className = "tm-nav-item nav_login";
        } else if (name === "login") {
            document.querySelector(".nav_home").className = "nav_home tm-nav-item";
            document.querySelector(".nav_about").className = "tm-nav-item nav_about";
            document.querySelector(".nav_contact").className = "tm-nav-item nav_contact";
            document.querySelector(".nav_login").className = "tm-nav-item active nav_login";
        }
    }
    return (
        <header className="tm-header" id="tm-header">
            <div className="tm-header-wrapper">
                <button className="navbar-toggler" type="button" aria-label="Toggle navigation">
                    <i className="fas fa-bars"></i>
                </button>
                <nav className="tm-nav" id="tm-nav">
                    <ul>
                        <li className="tm-nav-item active nav_home" onClick={() => active("home")}><Link to="/" className="tm-nav-link">
                            <i className="fas fa-home"></i>
                            Home
                        </Link></li>
                        <li className="tm-nav-item nav_login" onClick={() => active("login")}><Link to="/post" className="tm-nav-link">
                            <i className="fas fa-pen"></i>
                            ADD SERVICE
                        </Link></li>
                        <li className="tm-nav-item nav_about" onClick={() => active("about")}><Link to="/about" className="tm-nav-link">
                            <i className="fas fa-users"></i>
                            About
                        </Link></li>
                        <li className="tm-nav-item nav_contact" onClick={() => active("contact")}><Link to="/contact" className="tm-nav-link">
                            <i className="far fa-comments"></i>
                            Contact
                        </Link></li>
                    </ul>
                </nav>
                <div className="tm-mb-65">
                    <a rel="nofollow" href="https://fb.com/templatemo" className="tm-social-link">
                        <i className="fab fa-facebook tm-social-icon"></i>
                    </a>
                    <a href="https://twitter.com" className="tm-social-link">
                        <i className="fab fa-twitter tm-social-icon"></i>
                    </a>
                    <a href="https://instagram.com" className="tm-social-link">
                        <i className="fab fa-instagram tm-social-icon"></i>
                    </a>
                    <a href="https://linkedin.com" className="tm-social-link">
                        <i className="fab fa-linkedin tm-social-icon"></i>
                    </a>
                </div>
                <p className="tm-mb-80 pr-5 text-white">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda ducimus facilis inventore nobis quisquam. Accusantium doloremque laudantium neque soluta suscipit!
                </p>
            </div>
        </header>
    );
};

export default Navbar;
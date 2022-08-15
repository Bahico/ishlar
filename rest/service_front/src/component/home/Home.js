import React from 'react';
import "./css/bootstrap.min.css";
import "./css/templatemo-xtra-blog.css"
import ServiceArr from "../services/ServiceArr";

const Home = () => {
    return (
        <div>
            <div className="container-fluid">
                <main className="tm-main">
                    <div className="row tm-row">
                        <div className="col-12">
                            <form method="GET" className="form-inline tm-mb-80 tm-search-form">
                                <input className="form-control tm-search-input" name="query" type="text"
                                       placeholder="Search..." aria-label="Search" />
                                    <button className="tm-search-button" type="submit">
                                        <i className="fas fa-search tm-search-icon" aria-hidden="true"></i>
                                    </button>
                            </form>
                        </div>
                    </div>
                    <div className="row tm-row">
                        <ServiceArr />
                    </div>
                    <footer className="row tm-row">
                        <hr className="col-12" />
                            <div className="col-md-6 col-12 tm-color-gray tm-copyright">
                                Copyright 2020 Xtra Blog Company Co. Ltd.
                            </div>
                    </footer>
                </main>
            </div>
        </div>
    );
};

export default Home;
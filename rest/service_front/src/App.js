import React from "react";
import {Route,Switch} from "react-router-dom"
import Navbar from "./component/navbar/Navbar";
import Login from "./component/login/Login";
import SignUp from "./component/login/SignUp";
import Home from "./component/home/Home"
import ServiceArr from "./component/services/ServiceArr";
import ServiceItem from "./component/services/ServiceItem";
import './App.css'
import AddPost from "./component/AddPost";

function App() {

  const token = localStorage.getItem("token")
  return (
    <div className="App">
      <Navbar />
      {
        token
          ?
            <Switch>
              <Route path="*">
                <h1>Error</h1>
              </Route>
            </Switch>
            :
            <Switch>
              <Route path="/" exact>
                <Home />
              </Route>
                <Route path="/post" exact>
                    <AddPost />
                </Route>
              <Route path="/login" exact>
                <Login />
              </Route>
              <Route path="/create" exact>
                <SignUp />
              </Route>
              <Route path="/services">
                <ServiceArr />
              </Route>
                <Route path="/service/:id">
                    <ServiceItem />
                </Route>
              <Route path="*">
                <h1>Error</h1>
              </Route>
            </Switch>
      }

    </div>
  );
}

export default App;

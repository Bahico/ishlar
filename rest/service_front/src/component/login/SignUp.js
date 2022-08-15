import React, {useState} from 'react';
import "./login.css"
import {Link, useHistory} from "react-router-dom";
import axios from "axios";

const SignUp = () => {
    const history = useHistory()
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const signup = (e) => {
        axios.post("http://127.0.0.1:8000/user/create/", {
            method: "POST",
            data: {
                "id": 5,
                "username": username,
                "email": email,
                "password": password
            }
        }).then(r =>{})
        history.push("/login")
    }

    return (
        <div>
            <form className="login" onSubmit={signup}>
                <input type="text" placeholder="Username" value={username} onChange={e=>setUsername(e.target.value)}/>
                <input type="text" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)}/>
                <input type="password" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)}/>
                <Link to='/login' style={{display: "block", color: "rgba(0,0,0,.5)", textDecoration: "none"}}>Login</Link>
                <button>Login</button>
            </form>
        </div>
    );
};

export default SignUp;
import React, {useState} from 'react';
import "./login.css"
import {Link} from "react-router-dom";
import axios from "axios";

const Login = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const login = (e) => {
        e.preventDefault()
        axios.post('http://127.0.0.1:8000/user/login/',{
            data: {
                "username": username,
                "password": password
            }
        }).then(res => {

        })
    }

    return (
        <div>
            <form className="login" onSubmit={login}>
                <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)}/>
                <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
                <Link to='/create' style={{display: "block", color: "rgba(0,0,0,.5)", textDecoration: "none"}}>Create your account</Link>
                <button>Login</button>
            </form>
        </div>
    );
};

export default Login;
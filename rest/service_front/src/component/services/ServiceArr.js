import React, {useEffect, useState} from 'react';
import axios from "axios";
import Loading from "../loader/Loading";
import Service from "./Service";
import "./service.css"
import {Link} from "react-router-dom";
import Pagination from "../utils/Pagination";
import {useSelector} from "react-redux";

const ServiceArr = () => {
    const [services, setServices] = useState([])
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/task/service/10",{
            method: "POST"
        }).then(res => {
            if (res.data !== "Not post!"){
                setServices(res.data)
            }
        }).catch(error => {
            console.log(error)
        })
    }, [])
    const { posts } = useSelector((state) => state.posts);
    console.log(posts)
    return (
        <div>
        <div className="row tm-row">
                {!services ? <Loading/> : services.map(function (post) {
                    return <Service key={post.id} post={post} id={post.id}/>
                })
                }
                <div className="row tm-row tm-mt-100 tm-mb-75">
                    <div className="tm-prev-next-wrapper">
                        <Link to="/" className="mb-2 tm-btn tm-btn-primary tm-prev-next disabled tm-mr-20">Prev</Link>
                        <Link to="/" className="mb-2 tm-btn tm-btn-primary tm-prev-next">Next</Link>
                    </div>
                    <Pagination pageSize={Math.floor(services.length/10+1)} current={1} />
                </div>
            </div>
        </div>
    );
};

export default ServiceArr;
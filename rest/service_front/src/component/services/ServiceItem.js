import React, {useEffect, useState} from 'react';
import "./service.css"
import {useHistory, useParams} from "react-router-dom";
import './test.css'
import 'antd/dist/antd.css';
import axios from "axios";
import Loading from "../loader/Loading";
import MainComment from "../comment/MainComment";



const ServiceItem = () => {
    const {id} = useParams()
    const [post, setPost] = useState(null)
    const [photo, setPhoto] = useState("https://cdn.uzmovi.com/v1/images/noavatar.png?v=2.5.1")
    const history = useHistory()
    const [like, setLike] = useState(0)
    const [disLike, setDisLike] = useState(0)

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/task/detail/" + id, {
            method: "POST"
        }).then(res => {
            setPost(res.data)
            setDisLike(res.data.dislike)
            setLike(res.data.like)
        }).catch(error => {
            console.log(error)
        })
        axios.get("http://127.0.0.1:8000/task/photo/" + id, {
            responseType: "blob"
        }).then(res => {
            setPhoto(URL.createObjectURL(res.data))
        }).catch(error => {
            console.log(error)
        })

    }, [])

    const delService = () => {
        axios.get('http://127.0.0.1:8000/task/delete/'+id).then(()=>{})
        history.push('/')
    }

    const likeFunc = (name) => {
        const id = post.id
        if (name === "like") {
            if (document.querySelector(".service--dislike").className === "btn btn-light service--dislike") {
                if (document.querySelector(".service--like").className === "btn btn-light service--like") {
                    axios.get("http://127.0.0.1:8000/task/like-add/"+id).then(() => {})
                    document.querySelector('.service--like').className = "btn btn-light service--like active"
                    setLike(like+1)
                } else {
                    axios.get("http://127.0.0.1:8000/task/like-del/"+id).then(() => {})
                    document.querySelector('.service--like').className = "btn btn-light service--like"
                    setLike(like-1)
                }
            } else {
                axios.get("http://127.0.0.1:8000/task/dislike-del/"+id).then(() => {})
                document.querySelector(".service--dislike").className = "btn btn-light service--dislike"
                axios.get("http://127.0.0.1:8000/task/like-add/"+id).then(() => {})
                document.querySelector('.service--like').className = "btn btn-light service--like active"
                setDisLike(disLike-1)
                setLike(like+1)
            }
        } else {
            if (document.querySelector(".service--like").className === "btn btn-light service--like") {
                if (document.querySelector(".service--dislike").className === "btn btn-light service--dislike") {
                    axios.get("http://127.0.0.1:8000/task/dislike-add/"+id).then(() => {})
                    document.querySelector('.service--dislike').className = "btn btn-light service--dislike active"
                    setDisLike(disLike+1)
                } else {
                    axios.get("http://127.0.0.1:8000/task/dislike-del/"+id).then(() => {})
                    document.querySelector('.service--dislike').className = "btn btn-light service--dislike"
                    setDisLike(disLike-1)
                }
            } else {
                axios.get("http://127.0.0.1:8000/task/like-del/"+id).then(() => {})
                document.querySelector(".service--like").className = "btn btn-light service--like"
                axios.get("http://127.0.0.1:8000/task/dislike-add/"+id).then(() => {})
                document.querySelector('.service--dislike').className = "btn btn-light service--dislike active"
                setDisLike(disLike+1)
                setLike(like-1)
            }
        }
    }


    return (
        <div className="container-fluid">
            {
                post ?
                    <main className="tm-main">
                        <div className="row tm-row">
                            <div className="col-12">
                                <hr className="tm-hr-primary tm-mb-55"/>
                                <img src={photo} alt="" style={{width: "500px"}}/>
                            </div>
                        </div>
                        <div className="row tm-row">
                            <div className="col-lg-8 tm-post-col">
                                <div className="tm-post-full">
                                    <div className="mb-4">
                                        <h2 className="pt-2 tm-color-primary tm-post-title">{post.title}</h2>
                                        <p className="tm-mb-40">{post.date}</p>
                                        <p>{post.description}</p>
                                        <div style={{display: "flex"}}>
                                            <div style={{marginRight:"50px"}}>
                                                <button className="btn btn-light service--like" onClick={()=>likeFunc('like')}><i className="fa fa-thumbs-up"></i></button>
                                                <br />
                                                <span>{ like }</span>
                                            </div>
                                            <div style={{marginRight:"50px"}}>
                                                <button className="btn btn-light service--dislike" onClick={()=>likeFunc('dislike')}><i className="fa fa-thumbs-down"></i></button>
                                                <br/>
                                                <span>{ disLike }</span>
                                            </div>
                                            <div style={{marginRight:"50px"}}>
                                                <button className="btn btn-light service--dislike" disabled><i className="fa fa-eye"></i></button>
                                                <br/>
                                                <span>{ post.views + 1 }</span>
                                            </div>
                                            <button className="btn btn-danger" onClick={()=>delService()}>DELETE</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </main> :
                <Loading/>
            }

    </div>
    );
};

export default ServiceItem;
import React, {useState,useEffect} from 'react';
import "./service.css"
import {Link} from "react-router-dom";
import axios from "axios";

const Service = (props) => {
    const [image, setPhoto] = useState("")
    const [like, setLike] = useState(props.post.like)
    const [disLike, setDisLike] = useState(props.post.dislike)
    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/task/photo/${props.id}`,{
            method: "POST",
            responseType: "blob"
        }).then(res => {
            setPhoto(URL.createObjectURL(res.data))
        }).catch(error => {
            console.log(error)
        })
    }, [])


    const likeFunc = (name, id) => {
        if (name === "like") {
            if (document.querySelector(".service-dislike").className === "btn btn-light service-dislike") {
                if (document.querySelector(".service-like").className === "btn btn-light service-like") {
                    axios.get("http://127.0.0.1:8000/task/like-add/"+id).then(() => {})
                    document.querySelector('.service-like').className = "btn btn-light service-like active"
                    setLike(like+1)
                } else {
                    axios.get("http://127.0.0.1:8000/task/like-del/"+id).then(() => {})
                    document.querySelector('.service-like').className = "btn btn-light service-like"
                    setLike(like-1)
                }
            } else {
                axios.get("http://127.0.0.1:8000/task/dislike-del/"+id).then(() => {})
                document.querySelector(".service-dislike").className = "btn btn-light service-dislike"
                axios.get("http://127.0.0.1:8000/task/like-add/"+id).then(() => {})
                document.querySelector('.service-like').className = "btn btn-light service-like active"
                setDisLike(disLike-1)
                setLike(like+1)
            }
        } else {
            if (document.querySelector(".service-like").className === "btn btn-light service-like") {
                if (document.querySelector(".service-dislike").className === "btn btn-light service-dislike") {
                    axios.get("http://127.0.0.1:8000/task/dislike-add/"+id).then(() => {})
                    document.querySelector('.service-dislike').className = "btn btn-light service-dislike active"
                    setDisLike(disLike+1)
                } else {
                    axios.get("http://127.0.0.1:8000/task/dislike-del/"+id).then(() => {})
                    document.querySelector('.service-dislike').className = "btn btn-light service-dislike"
                    setDisLike(disLike-1)
                }
            } else {
                axios.get("http://127.0.0.1:8000/task/like-del/"+id).then(() => {})
                document.querySelector(".service-like").className = "btn btn-light service-like"
                axios.get("http://127.0.0.1:8000/task/dislike-add/"+id).then(() => {})
                document.querySelector('.service-dislike').className = "btn btn-light service-dislike active"
                setDisLike(disLike+1)
                setLike(like-1)
            }
        }
    }




    return (
        <article className="col-12 col-md-6 tm-post">
            <hr className="tm-hr-primary" />
            <Link to={`service/${props.id}`} onClick={()=>axios.get("http://127.0.0.1:8000/task/views/" + props.id).then(()=>{})} className="effect-lily tm-post-link tm-pt-60">
                <div className="tm-post-link-inner">
                    <img src={image} alt="Image" className="img-fluid" />
                </div>
                <h2 className="tm-pt-30 tm-color-primary tm-post-title">{ props.post.title }</h2>
            </Link>
            <p className="tm-pt-30">{ props.post.description }</p>
            <div className="d-flex justify-content-between tm-pt-45">
                <span className="tm-color-primary">Service information</span>
                <span className="tm-color-primary">{ props.post.date }</span>
            </div>
            <hr />
            <div className="d-flex justify-content-between" style={{display:"flex",position:"absolute"}}>
                <div style={{marginRight:"50px"}}>
                    <button className="btn btn-light service-like" onClick={()=>likeFunc('like', props.post.id)}><i className="fa fa-thumbs-up"></i></button>
                    <br />
                    <span>{ like }</span>
                </div>
                <div>
                    <button className="btn btn-light service-dislike" onClick={()=>likeFunc('dislike', props.post.id)}><i className="fa fa-thumbs-down"></i></button>
                    <br/>
                    <span>{ disLike }</span>
                </div>
            </div>
        </article>
    );
};



export default Service;

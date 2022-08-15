import Loading from "../loader/Loading";
import React, {useEffect, useState} from "react";
import axios from "axios";
import {useParams} from "react-router-dom";
import {useDispatch, useSelector} from "react-redux";
// import {decrement, main} from "../../redux/counter";

export const CommentsMap = () => {
    const { comments } = useSelector((state) => state.counter);
    const {id} = useParams()
    const delComment = id => {
        axios.get("http://127.0.0.1:8000/comment/delete/"+id).then(()=>{})
        // dispatch(decrement(id))
    }
    if (comments) {
        return (comments.map(e => <div className="tm-comment tm-mb-45" key={e.id}>
            <figure className="tm-comment-figure">
                {e.photo ?
                    <Photo id={e.id} title={e.title} />
                    :
                    <img src="https://cdn.uzmovi.com/v1/images/noavatar.png?v=2.5.1"
                         alt="Image"
                         className="mb-2 rounded-circle img-thumbnail"/>
                }
                <figcaption className="tm-color-primary text-center">{e.full_name}</figcaption>
            </figure>
            <div>
                <p>{e.description}</p>
                <div className="d-flex justify-content-between">
                    <a href="#" className="tm-color-primary">REPLY</a>
                    <span className="tm-color-primary" style={{marginLeft: "20px", marginRight: "20px"}}>June 14, 2020</span>
                    <button className="btn btn-danger" onClick={() => delComment(e.id)}>DELETE</button>
                </div>
            </div>
        </div>))
    } else {
        return <Loading />
    }
}


const Photo = ({id, title}) => {
    const [img,setImg] = useState('')
    useEffect(() => {
            axios.get('http://127.0.0.1:8000/comment/photo/' + id, {
                responseType: "blob"
            }).then(res => {
                if (res.data !== "Not comment img") {
                    setImg(URL.createObjectURL(res.data))
                }
            })
        }
    , [])

    return <img src={img} alt={title} className="mb-2 img-thumbnail" style={{width: "100px", maxHeight: "150px"}} />
}
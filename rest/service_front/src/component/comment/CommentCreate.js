import React, {useState} from 'react';
import axios from "axios";
import {useParams} from "react-router-dom";
import {useDispatch} from "react-redux";
import {increment} from "../../redux/counter";



const CommentCreate = () => {
    const {id} = useParams()
    const [full_name, setFullName] = useState("")
    const [comment, setComment] = useState("")
    const [file, setFile] = useState(false)
    const dispatch = useDispatch();
    const commentCreate = (e) => {

        const commentCreate = new FormData()
        commentCreate.append('id', 5);
        commentCreate.append('post_id', id);
        commentCreate.append("full_name", full_name);
        commentCreate.append("description", comment);
        if (file !== false) {
            commentCreate.append("photo", file, file.name)
        }
        commentCreate.append("like", 0);
        commentCreate.append("dislike", 0);
        axios.post("http://127.0.0.1:8000/comment/create/", commentCreate)
            .then(res => {
                dispatch(increment({
                    'id': res.data,
                    'post_id': id,
                    'full_name': full_name,
                    'description': comment,
                    'photo': file
                }))
            })
        setComment("")
        setFullName("")
        setFile("")
    }
    return (
        <div>
            <form className="mb-5 tm-comment-form" onSubmit={commentCreate}>
                <h2 className="tm-color-primary tm-post-title mb-4">Your comment</h2>
                <div className="mb-4">
                    <input className="form-control" name="name" type="text"
                           placeholder="Full name" value={full_name}
                           onChange={(e) => setFullName(e.target.value)} required/>
                </div>
                <div className="mb-4">
                    <textarea className="form-control" name="message" rows="6"
                              value={comment} onChange={(e) => setComment(e.target.value)}
                    ></textarea>
                </div>
                <div className="mb-4">
                    <input type="file" className="form-control"
                           onChange={event => setFile(event.target.files[0])} />
                </div>
                <div className="text-right">
                    <button className="tm-btn tm-btn-primary tm-btn-small">Submit</button>
                </div>
            </form>
        </div>
    );
};

export default CommentCreate;
import React, {useState} from 'react';
import './services/test.css'
import 'antd/dist/antd.css';
import axios from "axios";

const AddPost = () => {
    const [full, setFull] = useState("")
    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")
    const [file, setFile] = useState("")
    const [encodedImage, setEncodedImage] = useState("")

    const addPost = (e) => {
        e.preventDefault()
        const uploadData = new FormData();
        uploadData.append('id',5);
        uploadData.append('user',full);
        uploadData.append('title',title);
        uploadData.append('description',description);
        uploadData.append('photo',file,file.name);
        uploadData.append('date','2015-03-25');
        uploadData.append('like',0);
        uploadData.append('dislike',0);
        uploadData.append('views',0);
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function () {
            // const formData = new FormData();
            // formData.append("file", file, file.name);
            setEncodedImage(reader.result);
            axios.post("http://127.0.0.1:8000/task/create/", uploadData).then(r => {
                setFile("")
                setFull("")
                setTitle("")
                setDescription("")
            })
        };
        reader.onerror = function (error) {
            console.log('Error: ', error);
        };
    }

    const setImage = event => {
        setFile(event.target.files[0])
    }


    return (<div>
        <form className="mb-5 w-50" style={{marginLeft: "500px"}} onSubmit={addPost}>
            <h2 className="tm-color-primary tm-post-title mb-4">Add service</h2>
            <div className="mb-4">
                <input className="form-control" name="name" type="text" placeholder="Full name"
                       value={full} onChange={e => setFull(e.target.value)} required />
            </div>
            <div className="mb-4">
                <input className="form-control" name="name" type="text" placeholder="Title" value={title}
                       onChange={e => setTitle(e.target.value)} required />
            </div>
            <div className="mb-4">
                    <textarea className="form-control" name="message" rows="6" value={description}
                              onChange={e => setDescription(e.target.value)} required ></textarea>
            </div>
            <div className="mb-4">
                <input type="file" className="form-control" onChange={setImage} required/>
            </div>
            <div className="text-right">
                <button className="tm-btn tm-btn-primary tm-btn-small">Submit</button>
            </div>
        </form>
    </div>);
};

export default AddPost;
import React from 'react';
import {useForm} from "react-hook-form";
import app from "../App";

const Sino = () => {
    const {register, handleSubmit} = useForm();

    const onSubmit = data => {
        const storageRef = app.storage().ref();
        const fileRef = storageRef.child(data.image[0].name);
        fileRef.put(data.image[0]).then(()=> {
            console.log("Upload a file");
        });
    }
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="file" ref={register} required name="image"/>
            <button>Submit</button>
        </form>
    );
};

export default Sino;
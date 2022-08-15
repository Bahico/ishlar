import React from 'react';
import {CommentsMap} from "./CommentArr";
import CommentCreate from "./CommentCreate";

const MainComment = () => {

    return (
        <div>
            <h2 className="tm-color-primary tm-post-title">Comments</h2>
            <hr className="tm-hr-primary tm-mb-45"/>
            <div>
                <CommentsMap />
                <CommentCreate />
            </div>
        </div>
    );
};

export default MainComment;
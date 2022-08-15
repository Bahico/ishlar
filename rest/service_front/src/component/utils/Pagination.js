import React from 'react';
import {Link} from "react-router-dom";
import {} from "react-redux"

const Pagination = ({pageSize, current}) => {
    const pageArray = [];
    for (let i = 0; i < pageSize; i++) {
        pageArray.push(i + 1);
    }
    const paginationItemClass = (idx) => `tm-paging-item  ${current === idx ? "active" : ""}`
    let i = 0;
    const pageItems = pageArray.map(idx =>{
        i += 1;
        return <li className={paginationItemClass(idx)} key={i}>
                    <Link to={"/"} className="mb-2 tm-btn tm-paging-link">{idx}</Link>
                </li>
    })
    return (<div className="tm-paging-wrapper">
        <span className="d-inline-block mr-3">Page</span>
        <nav className="tm-paging-nav d-inline-block">
            <ul>
                {pageItems}
            </ul>
        </nav>
    </div>);
}

export default Pagination;
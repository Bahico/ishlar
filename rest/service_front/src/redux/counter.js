import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";


export const counterSlice = createSlice({
    name: "comment",
    initialState: {
        count: []
    },
    reducers: {
        increment: (state,action) => {
            state.count.push(action.payload);
        },
        decrement: (state,action) => {
            for(let i = 0; i < state.count.length; i++){
                if ( state.count[i] === action.payload) {
                    state.count.splice(i, 1);
                }
            }
        },
        main: (state,action) => {
            axios.get(`http://127.0.0.1:8000/comment/detail/${action.payload}/10`)
                .then(res => {
                    if (res.data !== "Not comment!") {
                         state.count = res.data
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
})

export const { increment, decrement, main } = counterSlice.actions
export default counterSlice.reducer;
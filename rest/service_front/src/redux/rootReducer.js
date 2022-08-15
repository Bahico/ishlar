import {combineReducers} from 'redux'

function commentReducer(state = [], action) {
    if (action.type === "INCREMENT") {
        return state.push(action.payload)
    } else if (action.type === "DECREMENT") {
        return state.filter(e=>e.id!==action.payload)
    }

    return state
}

function postsReducer(state = [], action) {
    if (action.type === "INCREMENT") {
        return state.push(action.payload)
    } else if (action.type === "DECREMENT") {
        return state.filter(e=>e.id!==action.payload)
    }
    return state
}

export const rootReducer = combineReducers({
    counter: commentReducer,
    posts: postsReducer
})
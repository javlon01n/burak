import express from "express";
import path from "path";
import router from "./router";
import routerAdmin from "./routerAdmin";

//Expressni 4ta bo'lomi mavjud
/**  1-ENTRANCE **/
const app = express();
app.use(express.static(path.join(__dirname, "public")));
app.use(express.urlencoded({ extended: true}));
app.use(express.json());

/** 2-SESSIONS  **/


/** 3-VIEWS **/
app.set("views", path.join(__dirname, "views"));
app.set("views engine", "ejs");

/** 4-ROUTERS **/
app.use("/admin", routerAdmin) // SSE: EJS
app.use("/", router)  //  SPA: REACT, Middleware Design pattern

export default app;
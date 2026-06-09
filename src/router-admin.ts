import express from 'express';
const routerAdmin = express.Router();
import restaurantController from './controllers/restaurant.controller';

/** Restaurant */
routerAdmin.get("/", restaurantController.goHome);
routerAdmin
   .get("/Login", restaurantController.getLogin)
   .post("/Login", restaurantController.processLogin);
routerAdmin
.get("/signup", restaurantController.getSignup)
.post("/signup", restaurantController.processSignup);

routerAdmin.get("/check-me", restaurantController.checkAuthSession);

/** Product */
/** User */

export default routerAdmin;
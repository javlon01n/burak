import Viewmodel from "../schema/view.model";

class ViewService {
    private readonly viewmodel;

    constructor() {
        this.viewmodel = Viewmodel;
    }
}

export default ViewService;
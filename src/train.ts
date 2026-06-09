/*Project Standards:
- Logging stanadards:
- Naming standads:
   function, method, variable => CAMEL
    class => PASCAL    
    folder, file => KEBAB
    css => SNAKE
- Error handling

*/



/**
    Traditinal Api 
    Rest Api  
    GraphQL api
    ....
 */


/**
    Traditinal FD  =>  SSR  => EJS
    Modern FD.     =>  SPA  => REACT
 */ 



function hasProperty(obj: any, property: string): boolean {
    if (property in obj) {
        return true;
    } else {
        return false;
    }
}

console.log(hasProperty({ name: "BMW" }, "name"));
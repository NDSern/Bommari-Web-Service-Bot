import express, { Express, Request, Response } from "express";
import dotenv from "dotenv";
import Routes from "model";
import cors from "cors";

dotenv.config();

const app: Express = express();
const port = process.env.PORT || 3000;

app.use(cors())

app.get("/", (req: Request, res: Response) => {
    res.send("Express + TypeScript Server");
    Routes.findAll().then((res) => { console.log(res) })
});

app.listen(port, () => {
    console.log(`[server]: Server is running at http://localhost:${port}`);
});

app.get("/routes", (req: Request, res: Response) => {
    Routes.findAll({
        where: req.query,
        order: [
            ["id", "desc"]
        ]
    }).then(routes => { 
        res.json(routes)
    })
})

app.use('/public', express.static('../Database/public'))

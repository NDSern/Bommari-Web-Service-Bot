import express, { Express, Request, Response } from "express";
import dotenv from "dotenv";
import Routes from "model";
import cors from "cors";
import path from "node:path";
import https from "https";
import fs from "fs";

dotenv.config();

const app: Express = express();
const port = 443;


app.use(cors());

app.get("/", (req: Request, res: Response) => {
    res.sendFile(path.resolve("../Database/dist/index.html"));
});

const server = https.createServer({
    cert: fs.readFileSync(path.join(__dirname, "SSL", "fullchain.pem")),
    key: fs.readFileSync(path.join(__dirname, "SSL", "privkey.pem"))
}, app);

server.listen(port, () => {
    console.log(`[server]: Server is running at https://localhost:${port}`);
});

app.get("/routes", (req: Request, res: Response) => {
    Routes.findAll({
        where: req.query,
        order: [
            ["id", "desc"]
        ]
    }).then(routes => {
        res.json(routes);
    })
});

app.use('/public', express.static('../Database/public'));

app.use('/', express.static('../Database/dist'));

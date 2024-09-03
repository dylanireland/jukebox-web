import express from "express";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const port = 3000;

const app = express();
app.use(express.static(__dirname + "/dist"));

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/dist/index.html");
});

app.listen(port, "localhost", () => {
	console.log("Server running");
});

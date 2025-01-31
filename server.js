import express from "express";
import { fileURLToPath } from "url";
import { dirname } from "path";
const greenlock = await import("greenlock-express").then(module => module.default || module);

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
app.use(express.static(__dirname + "/dist"));

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/dist/index.html");
});

const greenlockApp = greenlock.init({
	packageRoot: __dirname,
	configDir: "./greenlock.d",
	maintainerEmail: "dylan.ireland777@gmail.com",
	cluster: false
});

greenlockApp.serve(app);

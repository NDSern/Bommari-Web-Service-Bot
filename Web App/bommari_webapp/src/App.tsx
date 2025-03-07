import Menu from "./components/Menu";
import CallRoutes from "./components/CallRoutes";
import { useEffect, useState } from "react";
import { Route } from "./types/route";

const API = "http://bommari.vraminhos.com:3000/routes";


export default function App() {
	let [routes, setRoutes] = useState<Route[]>([]);
	let [grade, setGrade] = useState<string>("all");
	let [angle, setAngle] = useState<string>("all");
	let [author, setAuthor] = useState<string>("all")
	let [filteredRoutes, setFilteredRoutes] = useState<Route[]>(routes);

	useEffect(() => {
		fetch(API)
			.then((response) => response.json())
			.then((data) => setRoutes(data));
	}, []);

	useEffect(() => {
		setFilteredRoutes(
			routes
				.filter((e) => angle == "all" ? true : e.angle == angle)
				.filter((e) => grade == "all" ? true : e.grade == grade)
				.filter((e) => author == "all" ? true : e.user == author)
		)
	}, [grade, angle, routes, author])

	return (
		<>
			<Menu routes={routes} setGrade={setGrade} setAngle={setAngle} setAuthor={setAuthor} />
			<CallRoutes routes={filteredRoutes} />
		</>
	);
}

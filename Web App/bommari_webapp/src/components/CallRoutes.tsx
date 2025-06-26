import Card from "react-bootstrap/Card";
import { Route } from "../types/route";
import { Collapse, Container, Form } from "react-bootstrap";
import { IoMdClose } from "react-icons/io";
import { IoFilterOutline } from "react-icons/io5";
import { Dispatch, SetStateAction, useState } from "react";

const PHOTO_API = "https://bommari.vraminhos.com/public/";

type RouteProps = {
	routes: Route[];
	filteredRoutes: Route[];
	setGrade: Dispatch<SetStateAction<string>>;
	setAngle: Dispatch<SetStateAction<string>>;
	setAuthor: Dispatch<SetStateAction<string>>;
	grade: string;
	angle: string;
	author: string;
}

export default function CallRoutes({ routes, filteredRoutes, setGrade, setAngle, setAuthor, grade, angle, author }: RouteProps) {
	const [open, setOpen] = useState(false);
	let grades = new Set(filteredRoutes.map((value) => value.grade))
	let newGrades = Array.from(grades).sort()
	let angles = new Set(filteredRoutes.map((value) => value.angle))
	let newAngle = [...angles].sort()
	let authors = new Set(filteredRoutes.map((value) => value.user))
	let newAuthor = [...authors].sort()
	if (routes)
		console.log("Yay");

	return (
		<Container className={"py-3"}>
			<p className={"alert alert-primary"}>
				<div className={"d-flex justify-content-between align-items-center"}>
					<span>Number of routes: {filteredRoutes.length}</span>
					<div>
						<span className={"btn"} onClick={() => setOpen(!open)}>
							<IoFilterOutline
								title={"Filter"}
								size={25}
							/>
						</span>
						<span className={"btn"} onClick={() => {
							setGrade("all");
							setAngle("all");
							setAuthor("all");
						}}>
							<IoMdClose
								title={"Clear filter"}
								size={25}
							/>
						</span>
					</div>
				</div>
				<Collapse in={open}>
					<div>
						<div className="mt-2 mb-1">Grade</div>
						<Form.Select onChange={(e) => setGrade(e.target.value)} value={grade}>
							<option value="all">Every grade</option>
							<option value="">Mysterious grade</option>
							{newGrades.map((grade) => {
								if (grade == "") return;
								return <option key={grade} value={grade}>{grade}</option>;
							})}
						</Form.Select>
						<div className="mt-3 mb-1">Angle</div>
						<Form.Select onChange={(e) => setAngle(e.target.value)} value={angle}>
							<option value="all">Every angle</option>
							{newAngle.map((angle) => (
								<option key={angle} value={angle}>{angle}</option>
							))}
						</Form.Select>
						<div className="mt-3 mb-1">Author</div>
						<Form.Select onChange={(e) => setAuthor(e.target.value)} value={author}>
							<option value="all">Every author</option>
							{newAuthor.map((author) => (
								<option key={author} value={author}>{author}</option>
							))}
						</Form.Select>
					</div>
				</Collapse>
			</p>
			<div className="row">
				{filteredRoutes.map((route) => (
					<div key={route.id} className="col-12 col-sm-4 col-xl-3">
						<div className="card mb-3 text-bg-light bg-light-subtle border-secondary shadow">
							<img className={"card-img-top"} src={PHOTO_API + route.photo} alt={"Route picture"} loading="lazy" />
							<div className="card-body">
								<Card.Title>{route.name}</Card.Title>
								<Card.Subtitle>{route.user}</Card.Subtitle>
								<p className={"card-text"}>
									{route.grade + " | " + route.angle + " degree"}
									<br />{route.desc}
								</p>
							</div>
						</div>
					</div>
				))}
			</div>
		</Container>
	);
}

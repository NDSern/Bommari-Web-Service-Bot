import { Dispatch, SetStateAction, useState } from "react";
import { Collapse, Container, Form, Image, } from "react-bootstrap";
import { Route } from "../types/route";

type MenuProps = {
	routes: Route[]
	setGrade: Dispatch<SetStateAction<string>>
	setAngle: Dispatch<SetStateAction<string>>
	setAuthor: Dispatch<SetStateAction<string>>
}

export default function Menu({ routes, setGrade: setGrade, setAngle: setAngle, setAuthor: setAuthor }: MenuProps) {
	const [open, setOpen] = useState(false)

	let grades = new Set(routes.map((value) => value.grade))
	let newGrades = Array.from(grades).sort()
	let angles = new Set(routes.map((value) => value.angle))
	let newAngle = [...angles].sort()
	let authors = new Set(routes.map((value) => value.user))
	let newAuthor = [...authors].sort()

	return (
		<div className="sticky-top">
			<Container className="bg-warning pt-2 pb-3" fluid>
				<div className="d-flex justify-content-between">
					<Image src="/public/cropped-cropped-tekiila_outline-1.png" width={"60rem"} height={"60rem"} />
					<Image src="/public/filter-solid.svg" width={"60rem"} height={"60rem"} onClick={() => setOpen(!open)} />
				</div>
				<Collapse in={open}>
					<div>
						<div className="mt-2 mb-1">Grade</div>
						<Form.Select onChange={(e) => setGrade(e.target.value)}>
							<option value="all">Every grade</option>
							<option value="">Mysterious grade</option>
							{newGrades.map((grade) => {
								if (grade == "") return;
								return <option key={grade} value={grade}>{grade}</option>
							})}
						</Form.Select>
						<div className="mt-3 mb-1">Angle</div>
						<Form.Select onChange={(e) => setAngle(e.target.value)}>
							<option value="all">Every angle</option>
							{newAngle.map((angle) => (
								<option key={angle} value={angle}>{angle}</option>
							))}
						</Form.Select>
						<div className="mt-3 mb-1">Author</div>
						<Form.Select onChange={(e) => setAuthor(e.target.value)}>
							<option value="all">Every author</option>
							{newAuthor.map((author) => (
								<option key={author} value={author}>{author}</option>
							))}
						</Form.Select>
					</div>
				</Collapse>
			</Container>
		</div>
	);
}

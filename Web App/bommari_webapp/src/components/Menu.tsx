import { Dispatch, SetStateAction, useState } from "react";
import { Collapse, Container, Form, Image, } from "react-bootstrap";
import { Route } from "../types/route";

type MenuProps = {
	routes: Route[]
	setGrade: Dispatch<SetStateAction<string>>
	setAngle: Dispatch<SetStateAction<string>>
}

export default function Menu({ routes, setGrade: setGrade, setAngle: setAngle }: MenuProps) {
	const [open, setOpen] = useState(false)

	let grades = new Set(routes.map((value) => value.grade))
	let newGrades = Array.from(grades).sort()
	let angle = new Set(routes.map((value) => value.angle))
	let newAngle = [...angle].sort()

	return (
		<div className="sticky-top">
			<Container className="bg-warning pt-2 pb-3" fluid>
				<div className="d-flex justify-content-between">
					<Image src="./src/assets/cropped-cropped-tekiila_outline-1.png" width={"60rem"} height={"60rem"} />
					<Image src="./src/assets/filter-solid.svg" width={"60rem"} height={"60rem"} onClick={() => setOpen(!open)} />
				</div>
				<Collapse in={open}>
					<div>
						<div className="mt-2 mb-1">Grade</div>
						<Form.Select onChange={(e) => setGrade(e.target.value)}>
							<option value="all">Every grade</option>
							<option value="">Mysterious grade</option>
							{newGrades.map((grade) => {
								if (grade == "") return;
								return <option value={grade}>{grade}</option>
							})}
						</Form.Select>
						<div className="mt-3 mb-1">Angle</div>
						<Form.Select onChange={(e) => setAngle(e.target.value)}>
							<option value="all">Every angle</option>
							{newAngle.map((angle) => (
								<option value={angle}>{angle}</option>
							))}
						</Form.Select>
					</div>
				</Collapse>
			</Container>
		</div>
	);
}

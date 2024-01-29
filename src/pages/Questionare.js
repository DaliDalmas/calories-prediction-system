export default function Questionare(){
    return (
        <div className="bg-sky-300">
            {/* Question 1 */}
            <label>Kind of exercise</label>
            <select name="cars" id="cars" form="carform">
                <option value="Running">Runnig</option>
                <option value="Walking">Walking</option>
            </select><br />
            {/* Question 2 */}
            <label>Elevation or Climb in meters</label>
            <input type="number" placeholder="0"/><br />
            {/* Question 3 */}
            <label>Duratioin of exercise in seconds</label>
            <input type="number" placeholder="0"/><br />
            {/* Question 3 */}
            <label>Distance covered in meters</label>
            <input type="number" placeholder="0"/><br />
            {/* Question 3 */}
            <label>Date and time when you took the exercise</label>
            <input type="datetime-local" />
        </div>
    )
}
import './App.css';
import Todo from './Todo';
import Person from './Person';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Todo user="react learner" />
        <Person name="hello" age="bye" />
      </header>
    </div>
  );
}

export default App;

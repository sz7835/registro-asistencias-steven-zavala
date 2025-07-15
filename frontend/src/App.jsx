import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState('Cargando...')

  useEffect(() => {
    fetch('http://127.0.0.1:5000/ping')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => {
        console.error('Error al conectar con Flask:', err)
        setMessage('Error al conectar con el backend')
      })
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '4rem' }}>
      <h1>Conexión con Flask:</h1>
      <p>{message}</p>
    </div>
  )
}

export default App

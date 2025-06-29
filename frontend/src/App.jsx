import { useState } from 'react'
import './App.css'
import LiveKitModal from './components/LiveKitModal';

function App() {
  const [showSupport, setShowSupport] = useState(false);

  const handleSupportClick = () => {
    setShowSupport(true)
  }

  return (
    <div className="app">
      <header className="header">
        <div className="logo">
          <span className="logo-icon">🏥</span>
          MediCare Hospital
        </div>
        <nav>
          <a href="#services">Services</a>
          <a href="#doctors">Doctors</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
      </header>

      <main>
        <section className="hero">
          <div className="hero-content">
            <div className="title-container">
              <h1>Quality Healthcare Services</h1>
              <p>Professional medical care with compassionate service and advanced technology</p>
              
              <div className="stats">
                <div className="stat">
                  <span className="stat-number">24/7</span>
                  <span className="stat-label">Emergency Care</span>
                </div>
                <div className="stat">
                  <span className="stat-number">50+</span>
                  <span className="stat-label">Specialist Doctors</span>
                </div>
                <div className="stat">
                  <span className="stat-number">15+</span>
                  <span className="stat-label">Years Experience</span>
                </div>
              </div>
            </div>

            {/* Prime Feature - Appointment Booking */}
            <div className="prime-feature">
              <div className="prime-feature-badge">
                <span>⭐ BOOK APPOINTMENT</span>
              </div>
              <div className="appointment-booking">
                <h2>📅 Schedule Your Consultation</h2>
                <p>Book an appointment with our experienced doctors and get the care you deserve</p>
                <div className="booking-actions">
                  <button className="book-now-btn" onClick={handleSupportClick}>
                    📅 Book Appointment
                  </button>
                  <button className="emergency-btn">
                    🚨 Emergency Care
                  </button>
                </div>
              </div>
            </div>
            
            <div className="search-bar">
              <div className="search-icon">🔍</div>
              <input type="text" placeholder='Search for doctors, services, or health information'></input>
              <button>
                <span>Search</span>
              </button>
            </div>
            
            <div className="features">
              <div className="feature">
                <div className="feature-header">
                  <span className="feature-icon">🩺</span>
                  <div className="feature-badge">EXPERT</div>
                </div>
                <h3>Medical Consultation</h3>
                <p>Consult with our experienced doctors for accurate diagnosis and treatment plans</p>
                <div className="feature-stats">
                  <span>✓ Board Certified</span>
                </div>
              </div>
              <div className="feature">
                <div className="feature-header">
                  <span className="feature-icon">💊</span>
                  <div className="feature-badge">PHARMACY</div>
                </div>
                <h3>Prescription Services</h3>
                <p>Complete pharmacy services with medication counseling and drug interaction checks</p>
                <div className="feature-stats">
                  <span>✓ Licensed Pharmacists</span>
                </div>
              </div>
              <div className="feature">
                <div className="feature-header">
                  <span className="feature-icon">📋</span>
                  <div className="feature-badge">RECORDS</div>
                </div>
                <h3>Health Records</h3>
                <p>Secure digital health records accessible to you and your healthcare providers</p>
                <div className="feature-stats">
                  <span>✓ HIPAA Compliant</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <button className="support-button" onClick={handleSupportClick}>
          <div className="button-icon">👨‍⚕️</div>
          <span>Talk to Doctor</span>
        </button>
      </main>

      {showSupport && <LiveKitModal setShowSupport={setShowSupport}/>}
    </div>
  )
}

export default App

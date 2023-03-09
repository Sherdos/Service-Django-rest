import React, { useState } from 'react';
import './Header.scss';
export default function Header() {
  const [showBurger, setShowBurger] = useState(false);
  const burgerFunc = () => {
    setShowBurger(!showBurger);
  };
  return (
    <>
      <header className="header">
        <div className="header__container container">
          <h2 className='header__logo'>cs</h2>
          <nav className="header__nav">
            <ul className={showBurger ? 'header__menu header__menu-show' : 'header__menu'}>
              <li className="header__menu-link">Главная</li>
              <li className="header__menu-link">О нас</li>
              <li className="header__menu-link">Отзывы</li>
              <li className="header__menu-link">Поиск</li>
              <div className="header__register1">
              <button className="header__register-btn">Регистрация/Войти</button>
            </div>
            </ul>
            <div className="mobile-btn" onClick={burgerFunc}>
            {showBurger ? <i className="fa-solid fa-xmark"></i> : <i className="fa-solid fa-bars fax"></i>}
          </div>
          </nav>
          <div className="header__register">
              <button className="header__register-btn">Регистрация/Войти</button>
            </div>
        </div>
      </header>
    </>
  )
}

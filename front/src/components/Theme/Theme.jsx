import React from 'react'
import './Theme.scss'
export default function Theme() {
  return (
    <>
      <div id="my_switcher" className="my_switcher">
        <ul>
          <li onClick={() => dispatch(setColorLight()) /*toggleTheme*/}>
            <a href="#" className="setColor light" style={{background: '#F0F2F5'}}>
              <span title="Light Mode">Light</span>
            </a>
          </li>
          <li onClick={() => dispatch(setColorDark()) /*toggleTheme*/}>
            <a href="#" className="setColor dark">
              <span title="Dark Mode">Dark</span>
            </a>
          </li>
        </ul>
      </div>
    </>
  )
}

import React, {useState} from 'react'
import assets from './asset_data.json'
import NftImages from './components/NftImages'
import './App.css'

const App = () => {
  const [assetList, setAssetList] = useState(assets["assets"])
  const [showOverlay, setShowOverlay] = useState(false)
  
  return (
    <div className='image-grid'>
      <NftImages imgs={assetList}/>
    </div>
  )
}

export default App
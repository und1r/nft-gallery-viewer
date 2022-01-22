import React from 'react'

const NftImage = ({imgdata}) => {
    
    return (
        <div className="content">
          <div className="content-overlay"></div>
          <img
            className='image'
            src={'assets/'.concat(imgdata.id).concat('.png')}></img>
          <div className="content-details fadeIn-bottom">
            <table className='expanded-table'>
              <tbody>
                <tr>
                  <td>
                    <h3><b>BOXES {imgdata.id.slice(3).padStart(3, '0')}</b></h3>
                  </td>
                </tr>
                {(imgdata.data.tags).map((tag) => (
                  <tr key={tag}>
                    <td>
                      <p>{tag}</p>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className='nft-table-info'>
            <table className='inner-nft-table'>
                <tbody>
                    <tr>
                        <td className='text-left'>
                            <p className={imgdata.data.rarity}>{imgdata.data.rarity}</p>
                        </td>
                        <td className='text-right'>
                            <p>{imgdata.id.slice(3).padStart(3, '0')}</p>
                        </td>
                    </tr>
                    <tr>
                      <td className='text-left'>
                        <p className='less-important'>{imgdata.data.tags.length} Attributes</p>
                      </td>
                    </tr>
                </tbody>
            </table>
            <a href={'assets/'.concat(imgdata.id).concat('.png')} target='_blank'>
              <button className='download-button'></button>
            </a>
          </div>
      </div>

    )
}

export default NftImage
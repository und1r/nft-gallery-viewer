import React from 'react'
import NftImage from './NftImage'

const NftImages = ({imgs}) => {
    return (
        <>
            {imgs.map(image => <NftImage key={image.id} imgdata={image}/>)}
        </>
    )
}

export default NftImages
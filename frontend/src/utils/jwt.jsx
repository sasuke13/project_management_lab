const LIFE_TIME_TO_UPDATE_MULTIPLIER = 1;

export const isTokenExpired = (token)=> {
    if (!token) {
        return true;
    }

    try {
        const tokenInfo = token.split('.')[1];
        const tokenInfoDecoded = window.atob(tokenInfo);
        const { exp, iat } = JSON.parse(tokenInfoDecoded);

        const tokenLeftTime = exp - Math.round(+ new Date() / 1000);
        const minLifeTimeForUpdate = (exp - iat) * LIFE_TIME_TO_UPDATE_MULTIPLIER;
        
        return tokenLeftTime < minLifeTimeForUpdate;
    }
    catch(e) {
        console.error(e);
        return true;
    }
}

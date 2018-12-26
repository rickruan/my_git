'use strict'

const crypto = require('crypto');

function aesEncrypt(data,key) {
    const cipher = crypto.createCipher('aes192',key);
    var crypted = cipher.update(data,'utf8','base64')
    crypted+= cipher.final('base64');
    return crypted;
}

function aesDecrypt(encrypted,key) {
    const decipher = crypto.createDecipher('aes192',key);
    var decrypted = decipher.update(encrypted,'base64','utf8')
    decrypted+= decipher.final('utf8');
    return decrypted;
}

var data = 'Hello, This is a secret message';
var key= 'hello123456';
var encrypted = aesEncrypt(data,key);
var decrypted = aesDecrypt(encrypted,key);

console.log('Plain text: ' + data);
console.log('Encrypted text: ' + encrypted);
console.log('Decrypted text: ' + decrypted);


// xiaoming's keys:
var ming = crypto.createDiffieHellman(512);
var ming_keys = ming.generateKeys();

var prime = ming.getPrime();
var generator = ming.getGenerator();

console.log('Prime of ming: ' + prime.toString('hex'));
console.log('Generator of ming: ' + generator.toString('hex'));

// xiaohong's keys:
var hong = crypto.createDiffieHellman(prime, generator);
var hong_keys = hong.generateKeys();

console.log('Generator of Hong: ' + hong_keys.toString('hex'));

// exchange and generate secret:
var ming_secret = ming.computeSecret(hong_keys);
var hong_secret = hong.computeSecret(ming_keys);

// print secret:
console.log('Secret of Xiao Ming: ' + ming_secret.toString('hex'));
console.log('Secret of Xiao Hong: ' + hong_secret.toString('hex'));
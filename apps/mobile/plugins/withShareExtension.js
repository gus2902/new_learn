const { withPlugins, withXcodeProject, withInfoPlist } = require('@expo/config-plugins')
const fs = require('fs')
const path = require('path')

function withShareExtension(config) {
  config = withInfoPlist(config, (config) => {
    config.modResults.CFBundleURLTypes = [
      ...(config.modResults.CFBundleURLTypes || []),
      {
        CFBundleURLSchemes: ['moments'],
      },
    ]
    return config
  })

  config = withXcodeProject(config, async (config) => {
    const xcodeProject = config.modResults
    const targetName = 'MomentsShareExtension'
    const bundleId = `${config.ios?.bundleIdentifier || 'com.moments.mindstudio'}.ShareExtension`

    const groupName = `${targetName}`
    if (!xcodeProject.pbxGroupByName(groupName)) {
      xcodeProject.addPbxGroup([], groupName, groupName)
    }

    console.log(`[withShareExtension] Share Extension target: ${targetName}`)
    console.log(`[withShareExtension] Bundle ID: ${bundleId}`)

    return config
  })

  return config
}

module.exports = withShareExtension

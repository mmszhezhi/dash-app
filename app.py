import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import json

# ========== 创建 Dash 应用 ==========
app = dash.Dash(__name__)
server = app.server
server = app.server

# ========== 扩展的暗色系主题字典 ==========
THEMES = {
    # ===== 经典暗色主题 =====
    'GitHub Dark': {
        'paper_bgcolor': '#0d1117',
        'plot_bgcolor': '#161b22',
        'font_color': '#c9d1d9',
        'grid_color': '#30363d',
        'line_color1': '#ff6b6b',
        'line_color2': '#4ecdc4',
        'line_color3': '#ffe66d',
        'card_bg': '#161b22',
        'button_bg': '#238636',
        'description': 'GitHub 风格深色主题'
    },
    'Darkly': {
        'paper_bgcolor': '#222222',
        'plot_bgcolor': '#2c2c2c',
        'font_color': '#ffffff',
        'grid_color': '#404040',
        'line_color1': '#00bc8c',
        'line_color2': '#3498db',
        'line_color3': '#f39c12',
        'card_bg': '#2c2c2c',
        'button_bg': '#00bc8c',
        'description': 'Bootstrap Darkly 主题'
    },
    'Slate': {
        'paper_bgcolor': '#272b30',
        'plot_bgcolor': '#3a3f44',
        'font_color': '#c8c8c8',
        'grid_color': '#4e5358',
        'line_color1': '#7a8288',
        'line_color2': '#62c462',
        'line_color3': '#f89406',
        'card_bg': '#3a3f44',
        'button_bg': '#7a8288',
        'description': 'Slate 石板灰主题'
    },
    'Cyborg': {
        'paper_bgcolor': '#000000',
        'plot_bgcolor': '#121212',
        'font_color': '#00ff00',
        'grid_color': '#333333',
        'line_color1': '#00ff00',
        'line_color2': '#ff00ff',
        'line_color3': '#00ffff',
        'card_bg': '#121212',
        'button_bg': '#00ff00',
        'description': 'Cyborg 赛博朋克主题'
    },
    'Vapor': {
        'paper_bgcolor': '#1a0b2e',
        'plot_bgcolor': '#2d1b4e',
        'font_color': '#ff71ce',
        'grid_color': '#4a2a6e',
        'line_color1': '#ff71ce',
        'line_color2': '#01cdfe',
        'line_color3': '#fffb96',
        'card_bg': '#2d1b4e',
        'button_bg': '#ff71ce',
        'description': 'Vapor 蒸汽波风格'
    },
    'Solarized Dark': {
        'paper_bgcolor': '#002b36',
        'plot_bgcolor': '#073642',
        'font_color': '#839496',
        'grid_color': '#194753',
        'line_color1': '#dc322f',
        'line_color2': '#268bd2',
        'line_color3': '#b58900',
        'card_bg': '#073642',
        'button_bg': '#268bd2',
        'description': 'Solarized 暖色深色主题'
    },
    
    # ===== 现代暗色主题 =====
    'Tokyo Night': {
        'paper_bgcolor': '#1a1b26',
        'plot_bgcolor': '#1f2335',
        'font_color': '#a9b1d6',
        'grid_color': '#2d3f5e',
        'line_color1': '#f7768e',
        'line_color2': '#9ece6a',
        'line_color3': '#e0af68',
        'card_bg': '#1f2335',
        'button_bg': '#7aa2f7',
        'description': 'Tokyo Night 东京之夜'
    },
    'Dracula': {
        'paper_bgcolor': '#282a36',
        'plot_bgcolor': '#44475a',
        'font_color': '#f8f8f2',
        'grid_color': '#6272a4',
        'line_color1': '#ff5555',
        'line_color2': '#50fa7b',
        'line_color3': '#f1fa8c',
        'card_bg': '#44475a',
        'button_bg': '#bd93f9',
        'description': 'Dracula 吸血鬼风格'
    },
    'One Dark': {
        'paper_bgcolor': '#282c34',
        'plot_bgcolor': '#2c313a',
        'font_color': '#abb2bf',
        'grid_color': '#3e4452',
        'line_color1': '#e06c75',
        'line_color2': '#98c379',
        'line_color3': '#e5c07b',
        'card_bg': '#2c313a',
        'button_bg': '#61afef',
        'description': 'Atom One Dark 主题'
    },
    'Nord': {
        'paper_bgcolor': '#2e3440',
        'plot_bgcolor': '#3b4252',
        'font_color': '#d8dee9',
        'grid_color': '#4c566a',
        'line_color1': '#bf616a',
        'line_color2': '#a3be8c',
        'line_color3': '#ebcb8b',
        'card_bg': '#3b4252',
        'button_bg': '#81a1c1',
        'description': 'Nord 北欧北极风格'
    },
    'Monokai': {
        'paper_bgcolor': '#272822',
        'plot_bgcolor': '#2d2e27',
        'font_color': '#f8f8f2',
        'grid_color': '#49483e',
        'line_color1': '#f92672',
        'line_color2': '#a6e22e',
        'line_color3': '#e6db74',
        'card_bg': '#2d2e27',
        'button_bg': '#f92672',
        'description': 'Monokai 经典编辑器主题'
    },
    
    # ===== 极简暗色主题 =====
    'Total Black': {
        'paper_bgcolor': '#000000',
        'plot_bgcolor': '#0a0a0a',
        'font_color': '#ffffff',
        'grid_color': '#1a1a1a',
        'line_color1': '#ffffff',
        'line_color2': '#888888',
        'line_color3': '#444444',
        'card_bg': '#0a0a0a',
        'button_bg': '#333333',
        'description': '极致全黑主题'
    },
    'Charcoal': {
        'paper_bgcolor': '#1a1a1a',
        'plot_bgcolor': '#242424',
        'font_color': '#e0e0e0',
        'grid_color': '#363636',
        'line_color1': '#6c63ff',
        'line_color2': '#ff6584',
        'line_color3': '#ffd166',
        'card_bg': '#242424',
        'button_bg': '#6c63ff',
        'description': '炭灰商务风格'
    },
    
    # ===== 科技/编程暗色主题 =====
    'VS Code Dark': {
        'paper_bgcolor': '#1e1e1e',
        'plot_bgcolor': '#252526',
        'font_color': '#d4d4d4',
        'grid_color': '#3d3d3d',
        'line_color1': '#ce9178',
        'line_color2': '#9cdcfe',
        'line_color3': '#d7ba7d',
        'card_bg': '#252526',
        'button_bg': '#007acc',
        'description': 'VS Code 编辑器主题'
    },
    'PyCharm Darcula': {
        'paper_bgcolor': '#2b2b2b',
        'plot_bgcolor': '#313335',
        'font_color': '#a9b7c6',
        'grid_color': '#464a4d',
        'line_color1': '#ff6b68',
        'line_color2': '#7ec699',
        'line_color3': '#f9b43a',
        'card_bg': '#313335',
        'button_bg': '#6897bb',
        'description': 'PyCharm Darcula 主题'
    },
    'Terminal': {
        'paper_bgcolor': '#0c0c0c',
        'plot_bgcolor': '#1a1a1a',
        'font_color': '#33ff33',
        'grid_color': '#2a2a2a',
        'line_color1': '#33ff33',
        'line_color2': '#ff3333',
        'line_color3': '#ffff33',
        'card_bg': '#1a1a1a',
        'button_bg': '#33ff33',
        'description': '复古终端风格'
    },
    
    # ===== 色彩丰富暗色主题 =====
    'Midnight Blue': {
        'paper_bgcolor': '#0a192f',
        'plot_bgcolor': '#112240',
        'font_color': '#8892b0',
        'grid_color': '#1d3d6d',
        'line_color1': '#64ffda',
        'line_color2': '#ff6b6b',
        'line_color3': '#f2a900',
        'card_bg': '#112240',
        'button_bg': '#64ffda',
        'description': '午夜深海蓝'
    },
    'Deep Purple': {
        'paper_bgcolor': '#1a0b2e',
        'plot_bgcolor': '#2d1b4e',
        'font_color': '#d4c1ec',
        'grid_color': '#4a2a6e',
        'line_color1': '#c084fc',
        'line_color2': '#f472b6',
        'line_color3': '#34d399',
        'card_bg': '#2d1b4e',
        'button_bg': '#8b5cf6',
        'description': '深邃紫色主题'
    },
    'Forest Night': {
        'paper_bgcolor': '#0d2818',
        'plot_bgcolor': '#14452f',
        'font_color': '#b7efc5',
        'grid_color': '#1f6d43',
        'line_color1': '#bbf0aa',
        'line_color2': '#ffd93d',
        'line_color3': '#ff8c42',
        'card_bg': '#14452f',
        'button_bg': '#4c9a2a',
        'description': '森林暗夜绿'
    },
    'Ocean Dark': {
        'paper_bgcolor': '#0a1929',
        'plot_bgcolor': '#0f2b3d',
        'font_color': '#b3e5fc',
        'grid_color': '#1a4a6e',
        'line_color1': '#4fc3f7',
        'line_color2': '#ff8a65',
        'line_color3': '#81c784',
        'card_bg': '#0f2b3d',
        'button_bg': '#0288d1',
        'description': '深海幽蓝主题'
    },
    
    # ===== 暖色调暗色主题 =====
    'Warm Dark': {
        'paper_bgcolor': '#1e1917',
        'plot_bgcolor': '#2d2421',
        'font_color': '#e8d5c4',
        'grid_color': '#4a3a35',
        'line_color1': '#e07a5f',
        'line_color2': '#81b29a',
        'line_color3': '#f2cc8f',
        'card_bg': '#2d2421',
        'button_bg': '#d65c39',
        'description': '暖棕色系暗色'
    },
    'Coffee': {
        'paper_bgcolor': '#24180a',
        'plot_bgcolor': '#362412',
        'font_color': '#d5c0a1',
        'grid_color': '#5a3d24',
        'line_color1': '#c9a87b',
        'line_color2': '#8ba88b',
        'line_color3': '#d4a373',
        'card_bg': '#362412',
        'button_bg': '#b97f48',
        'description': '咖啡暖棕色'
    }
}

# ========== 生成示例数据 ==========
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * 0.5 + 0.5

# ========== 创建图表函数 - 修复 titlefont 错误 ==========
def create_figure(theme_name, height=550):
    """根据主题名称创建图表，宽度自适应"""
    theme = THEMES[theme_name]
    
    fig = go.Figure()
    
    # 添加三条曲线
    fig.add_trace(go.Scatter(
        x=x, y=y1,
        mode='lines',
        name='正弦曲线 sin(x)',
        line=dict(width=2.5, color=theme['line_color1']),
        hovertemplate='x: %{x:.2f}<br>y: %{y:.3f}<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=x, y=y2,
        mode='lines',
        name='余弦曲线 cos(x)',
        line=dict(width=2.5, color=theme['line_color2']),
        hovertemplate='x: %{x:.2f}<br>y: %{y:.3f}<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=x, y=y3,
        mode='lines+markers',
        name='衰减正弦曲线',
        line=dict(width=1.8, color=theme['line_color3'], dash='dash'),
        marker=dict(size=3, symbol='circle'),
        hovertemplate='x: %{x:.2f}<br>y: %{y:.3f}<extra></extra>'
    ))
    
    # 设置布局 - 修复 titlefont 问题
    fig.update_layout(
        title=dict(
            text=f'📊 {theme_name} - {theme["description"]}',
            font=dict(size=18, color=theme['font_color']),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title=dict(
                text='X 轴 (弧度)',
                font=dict(color=theme['font_color'])
            ),
            tickfont=dict(color=theme['font_color']),
            gridcolor=theme['grid_color'],
            linecolor=theme['grid_color'],
            zerolinecolor=theme['grid_color']
        ),
        yaxis=dict(
            title=dict(
                text='Y 轴 数值',
                font=dict(color=theme['font_color'])
            ),
            tickfont=dict(color=theme['font_color']),
            gridcolor=theme['grid_color'],
            linecolor=theme['grid_color'],
            zerolinecolor=theme['grid_color']
        ),
        paper_bgcolor=theme['paper_bgcolor'],
        plot_bgcolor=theme['plot_bgcolor'],
        font=dict(color=theme['font_color']),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor=theme['paper_bgcolor'],
            font_size=12,
            font_family="Arial"
        ),
        legend=dict(
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor=theme['grid_color'],
            borderwidth=1,
            font=dict(size=12, color=theme['font_color']),
            x=0.02,
            y=0.98
        ),
        margin=dict(l=60, r=60, t=80, b=60),
        height=height,
        autosize=True
    )
    
    # 添加水平参考线
    fig.add_hline(y=0, line_width=1, line_dash="dash", line_color=theme['grid_color'], opacity=0.5)
    
    return fig

# ========== 自定义 CSS 样式 ==========
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>深色主题切换器</title>
        {%favicon%}
        {%css%}
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                overflow-x: hidden;
            }
            .theme-button {
                padding: 10px 15px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 13px;
                font-weight: 500;
                transition: all 0.2s ease;
                text-align: left;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            .theme-button:hover {
                transform: translateY(-1px);
                filter: brightness(1.1);
            }
            .control-panel {
                border-radius: 10px;
                margin-bottom: 20px;
                padding: 20px;
                transition: background-color 0.3s ease;
            }
            h1 {
                margin: 0 0 10px 0;
                font-size: 24px;
            }
            .info-text {
                font-size: 13px;
                margin-top: 15px;
                padding-top: 10px;
                border-top: 1px solid rgba(128, 128, 128, 0.3);
            }
            .button-container {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
                gap: 10px;
                margin-bottom: 10px;
                max-height: 280px;
                overflow-y: auto;
                padding: 5px;
            }
            .button-container::-webkit-scrollbar {
                width: 6px;
            }
            .button-container::-webkit-scrollbar-track {
                background: rgba(128, 128, 128, 0.2);
                border-radius: 3px;
            }
            .button-container::-webkit-scrollbar-thumb {
                background: rgba(128, 128, 128, 0.5);
                border-radius: 3px;
            }
            .graph-container {
                width: 100%;
                min-width: 0;
            }
            .js-plotly-plot, .plotly-graph-div {
                width: 100% !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# ========== Dash 应用布局 ==========
app.layout = html.Div(
    id='main-container',
    style={
        'minHeight': '100vh',
        'padding': '20px',
        'transition': 'background-color 0.3s ease',
        'backgroundColor': THEMES['GitHub Dark']['paper_bgcolor'],
        'width': '100%',
        'maxWidth': '100%',
        'overflowX': 'hidden'
    },
    children=[
        # 控制面板
        html.Div(
            id='control-panel',
            className='control-panel',
            style={
                'backgroundColor': THEMES['GitHub Dark']['card_bg'],
            },
            children=[
                html.H1('🎨 sssssfuck深色主sss题切换器xxxx', style={'color': THEMES['GitHub Dark']['font_color']}),
                html.P(f'共 {len(THEMES)} 个暗色系主题，点击下方按钮切换',
                       style={'marginBottom': '15px', 'color': THEMES['GitHub Dark']['font_color'],
                              'fontSize': '14px'}),
                
                # 主题按钮网格 - 直接展示所有按钮
                html.Div(
                    className='button-container',
                    children=[
                        html.Button(
                            theme_name,
                            id={'type': 'theme-button', 'index': theme_name},
                            className='theme-button',
                            style={
                                'backgroundColor': '#3a3a3a',
                                'color': '#ffffff',
                            },
                            title=theme_data['description']
                        )
                        for theme_name, theme_data in THEMES.items()
                    ]
                ),
                
                html.Div(
                    className='info-text',
                    style={'color': THEMES['GitHub Dark']['font_color']},
                    children=[
                        html.Span('✨ 当前主题: '),
                        html.Span(id='current-theme-display', children='GitHub Dark',
                                  style={'fontWeight': 'bold', 'color': THEMES['GitHub Dark']['line_color1']})
                    ]
                )
            ]
        ),
        
        # 图表容器 - 自适应宽度
        html.Div(
            className='graph-container',
            style={'width': '100%', 'minWidth': '0'},
            children=[
                dcc.Graph(
                    id='main-graph',
                    figure=create_figure('GitHub Dark'),
                    config={'displayModeBar': True, 'responsive': True},
                    style={'width': '100%'}
                )
            ]
        ),
        
        # 存储当前主题
        dcc.Store(id='current-theme', data='GitHub Dark'),
    ]
)

# ========== 回调函数：切换主题 ==========
@app.callback(
    [Output('main-graph', 'figure'),
     Output('main-container', 'style'),
     Output('control-panel', 'style'),
     Output('current-theme-display', 'children'),
     Output('current-theme-display', 'style'),
     Output('current-theme', 'data'),
     Output({'type': 'theme-button', 'index': dash.ALL}, 'style')],
    [Input({'type': 'theme-button', 'index': dash.ALL}, 'n_clicks')],
    [State('current-theme', 'data')]
)
def switch_theme(click_list, current_theme):
    """切换主题的回调函数"""
    ctx = dash.callback_context
    
    if not ctx.triggered:
        theme = current_theme
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id:
            button_dict = json.loads(button_id)
            theme = button_dict['index']
        else:
            theme = current_theme
    
    theme_config = THEMES[theme]
    
    # 创建新图表（自适应宽度）
    new_figure = create_figure(theme)
    
    # 更新主容器背景
    container_style = {
        'minHeight': '100vh',
        'padding': '20px',
        'transition': 'background-color 0.3s ease',
        'backgroundColor': theme_config['paper_bgcolor'],
        'width': '100%',
        'maxWidth': '100%',
        'overflowX': 'hidden'
    }
    
    # 更新控制面板样式
    panel_style = {
        'backgroundColor': theme_config['card_bg'],
        'borderRadius': '10px',
        'marginBottom': '20px',
        'padding': '20px',
        'transition': 'background-color 0.3s ease'
    }
    
    # 当前主题显示样式
    display_style = {
        'fontWeight': 'bold',
        'color': theme_config['line_color1']
    }
    
    # 更新所有按钮样式
    button_styles = []
    for name, data in THEMES.items():
        if name == theme:
            button_styles.append({
                'backgroundColor': data['button_bg'],
                'color': '#ffffff',
                'padding': '10px 15px',
                'border': 'none',
                'borderRadius': '6px',
                'cursor': 'pointer',
                'fontSize': '13px',
                'fontWeight': '500',
                'transition': 'all 0.2s ease',
                'textAlign': 'left',
                'whiteSpace': 'nowrap',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'boxShadow': '0 0 5px currentColor'
            })
        else:
            button_styles.append({
                'backgroundColor': '#3a3a3a',
                'color': '#ffffff',
                'padding': '10px 15px',
                'border': 'none',
                'borderRadius': '6px',
                'cursor': 'pointer',
                'fontSize': '13px',
                'fontWeight': '500',
                'transition': 'all 0.2s ease',
                'textAlign': 'left',
                'whiteSpace': 'nowrap',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis'
            })
    
    return new_figure, container_style, panel_style, theme, display_style, theme, button_styles

# ========== 运行应用 ==========
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)